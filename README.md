# Morningstar Cloud Day Presentation

Welcome to the content repo for my Cloud Day presentation, "Splunk Workshop: Modern Microservices Development with AWS SAM, Lambda and OpenTelemetry"

There will be additional content here to let folks that weren't able to attend replicate the in-person experience.  Keep checking back for more thorough documentation and tutorial guide.

In the meantime, these steps were my own personal workflow notes.  They may only make sense to me, but I hope to polish them soon.

Thank you SO much for following along, I'm excited to show some amazing technology :smile:

> **_NOTE:_**  The main content of each "stage" of the presentation are in the non-main branches (`01-xxx, 02-xxx, 03-xxx`).  `main` does not contain any demo code.

1. (Slide Deck) What is SAM?
   1. Why is it important
      1. Traditional Code Development Workflows; New Possibilities
   2. (Tom's Code) What does it do?
      1. `sam init` HelloWorld
      2. Explore Folder structure
         1. Lambda Code
         2. Events `sam local invoke "HelloWorldFunction" -e events/event.json`
         3. Local API Gateway `sam local start-api`
         4. Tests
            1. Unit
               1. `pip3 install -r tests/requirements.txt --user`
               2. `python3 -m pytest tests/unit -v`
            2. Integration
      3. Build & Deploy HelloWorld
         1. Walkthrough of `sam build` -> `.aws-sam`
         2. Walkthrough of `sam deploy --guided --capabilities CAPABILITY_NAMED_IAM`
         3. Review of deploy config file `samconfig.toml`
         4. Can supply Param values in here and never run `--guided` again
         5. Watch the deployment go down in real-time. **(TAKES ~ 3:30)**
         6. (AWS Console) Show it
   3. Introduce our "improved" Stock Trading app (Start at `01-base-application`)
      1. `git clone https://github.com/tjohander-splunk/morn-cloud-day.git && cd morn-cloud-day && git checkout 01-base-application`
         1. Explore Folder Structure
            1. Added 4 new Lambdas, peek at each layer a bit hard to see how they interact
            1. Added in a unit test `cd watchlist_updater && pytest test_handler.py`
            2. Added in a VPC to which the Lambdas are attached.  Why?  Real World & Otel Collector
            3. Added in a Step Function + ASL definition as our mechanism to exercise the application for us
               1. Deploy it
                  1. `sam build`
                  2. `sam deploy --guided` (Creates our first answer file)
                  3. **(TAKES ~ 5 Minutes)** STOP AND PAUSE FOR QUESTIONS, COMMENTS
               2. Take a tour in the Console:
                  1. CloudFormation UI 
                  2. Lambda UI
                  3. Step Functions UI
                     1. Let's Shoot off a Round of the Step Function
         2. I am going to set us up for our evolution and deploy quite a bit more to help us understand otel better
            1. `git checkout 02-auto-instrumentation`
            2. `sam build`
            3. Since we added some params, we need to save answers: `sam deploy --guided`
            4. _TAKE IT AWAY MIMI_ **(10-15 mins)**
2. (Slide Deck) What is OpenTelemetry?
   1. Why is it important
      1. Distributed Tracing
      1. Open Standards
      2. SDKs and an Aggregator ("Collector")
      2. Customized telemetry
3. (Tom's Code) Time travel to `02-auto-instrumentation`
   2. Give a tour
      3. What did we add?
         4. Instrumentation Layer
            5. What does that include?
         6. Env Vars
   8. (AWS Console) Exercise the app
4. (Tom's Code) Time travel to `03-manual-instrumentation`
   5. What did we add?
      6. Span Decoration
         7. What does that do?
            8. At a minimum, you get more context in your spans
            9. At a maximum you can use extensive features of a full-fledged distributed tracing platform...like _this_
         10. Show a few cool things in APM
      7. Telemetry mutation in the Collector
         1. Log in to EC2 Instance `ssh -i ~/.aws/tjohander-splunk-key-pair.pem ec2user@blah`
         2. open up the `gateway-config.yaml`
         3. ```
            processors:
              attributes/update:
                actions:
                  - key: alpaca.secret
                    value: redacted
                    action: update
            service:
              pipelines:
                traces:
                  processors:
                    - k8s_tagger
                    - batch
                    - resource
                    - resourcedetection
                    - attributes/update
            ```
         4. `sudo systemctl restart splunk-otel-collector.service`
