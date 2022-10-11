1. (Slide Deck) What is SAM?
   1. Why is it important
      1. Traditional Code Development Workflows; New Possibilities
   2. (Tom's Code) What does it do?
      3. Init Hello World
      4. Explore Folder structure
         8. Lambda Code
         9. Events
         9. Tests
           10. Unit
           11. Integration
         12. ... others??
      5. Deploy it
         12. Walkthough of `sam deploy --guided`
         13. Review of deploy config file `samconfig.toml`
           1. Can supply Param values in here and never run `--guided` again
         14. Watch the deployment go down in real-time.
         9. (AWS Console) Show it
   6. Introduce our "improved" Stock Trading app (Start at `01-Base-Application`)
      7. Explore Folder Structure
         8. Added in a unit test
         9. Added in a VPC to which the Lambdas are attached
         10. Added in a Step Function ASL definition as our mechanism to exercise the application for us
         11. Can provide an answer file
      8. Highlight the non-trivial amount of AWS infra that this application relies on
      8. Deploy it
      9. Now we wait....... (~12-15 minutes)
   7.  Like Sony and Cher or Beyonce and Jay-Z, there's a "better together" story that needs to be told!
2. (Slide Deck) What is OpenTelemetry
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