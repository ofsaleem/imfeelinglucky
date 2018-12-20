# imfeelinglucky
Slack command to provide the first Google result for a query

This uses AWS Lambda with a Python 2.7 runtime as well as an API Gateway.

You will need a mapping template in the APIGW integration request for content type `application/x-www-form-urlencoded` that reads:

```javascript
{
  "body" : $input.json('$')
}
```
