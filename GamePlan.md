1. (Slide Deck) What is SAM?
   1. Why is it important
      1. Traditional Code Development Workflows; New Possibilities
   2. (Tom's Code) What does it do?
      1. `sam init` HelloWorld
      3. Explore Folder structure
         8. Lambda Code
         9. Events
         9. Tests
           10. Unit
           11. Integration
         12. ... others??
      4. Deploy it
         11. Walkthrough of `sam build` -> `.aws-sam`
         12. Walkthough of `sam deploy --guided --capabilities CAPABILITY_NAMED_IAM`
         13. Review of deploy config file `samconfig.toml`
         14. Can supply Param values in here and never run `--guided` again
         15. Watch the deployment go down in real-time. **(TAKES ~ 3:30)**
         16. (AWS Console) Show it
   4. Introduce our "improved" Stock Trading app (Start at `01-Base-Application`)
      1. `cd ~/morn-cloud-day && git checkout 01-base-application`
         1. Explore Folder Structure
            1. Added in a unit test `cd watchlist_updater && pytest test_handler.py`
            2. Added in a VPC to which the Lambdas are attached.  Why?  Real World & Otel Collector
            3. Added in a Step Function + ASL definition as our mechanism to exercise the application for us
               1. Deploy it **(TAKES ~ 5 Minutes)** STOP AND PAUSE FOR QUESTIONS, COMMENTS GIFT CARD
            5. Like Sony and Cher or Beyonce and Jay-Z, there's a "better together" story that needs to be told!
            6. _I AM GOING TO SET US UP FOR OUR EVOLUTION AND DEPLOY QUITE A BIT MORE TO HELP US UNDERSTAND OTEL BETTER_
               1. `git checkout 02-auto-instrumentation`
               2. `sam build`
               3. `sam deploy --config-file samconfig-base`
2. (Slide Deck) What is OpenTelemetry (I SORTA THINK I SHOULD JUST CHECKOUT AND DEPLOUY THE CODE FOR STAGE 2 AT THIS POIUNT)
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
   7. Deploy the updates (See how easy this gets!)
   8. (AWS Console) Exercise the app
4. (Tom's Code) Time travel to `03-manual-instrumentation`
   5. What did we add?
      6. Span Decoration
         7. What does that do?
            8. At a minimum, you get more context in your spans
            9. At a maximum you can use extensive features of a full-fledged distributed tracing platform...like _this_
         10. Show a few cool things in APM
      11. Telemetry mutation in the Collector
          12. Show in our "back end"