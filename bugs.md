# Bugs founded in the project

## 1. Page footer is not aligned on the bottom of the page
### Steps to reproduce
1. Open the https://platform-qa.mytomorrows.com/home in a browser
2. Scroll to the bottom of the page
### Actual result
The footer (myt-footer) is not aligned on the bottom of the page. It is floating in the middle of the browser window.
### Expected result
The footer should be aligned on the bottom of the page.

## 2. /health-care-professional/{} returns 500 if registration_number don't pass validation
### Precondition
Use the following data:  
   ```
   country:11
   id_specialization:3
   is_involved_in_clinical_trial:true
   profession:"study_director"
   registration_number:"12345678"
   ```
### Steps to reproduce
1. Sign up with new user.
2. Go to https://platform-develop.mytomorrows.com/home
3. Click on Create account button.
4. On the next page fill in user sign up form -> Receive email with confirmation link.
5. Open email link to confirm registration
6. Fill specialisation form with the data from Precondition
7. Click on the Next button

Here is `curl` command to reproduce the issue:
```
curl 'https://microservice-develop.mytomorrows.com/v1.3.0/health-care-professional/21726954-6576-48fb-8871-4b11f647de65' \
  -X 'PATCH' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-GB,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uX2lkIjoiNDZiNmZiNTAtMTdjMS00YmFkLWFlYmEtZjk5MzFiNTc5Yjk2IiwidXNlcl9pZCI6MjUwNywidW5pcXVlX2lkIjoiMjE3MjY5NTQtNjU3Ni00OGZiLTg4NzEtNGIxMWY2NDdkZTY1IiwicG9ydGFsIjoiSENQIn0.FNzT99lH7S79vmQiB3pDldLJw8YiFBawoSxQCqTR2Pk' \
  -H 'origin: https://platform-develop.mytomorrows.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://platform-develop.mytomorrows.com/' \
  -H 'sec-ch-ua: "Chromium";v="125", "Not.A/Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36' \
  --data-raw '{"country":11,"id_specialization":3,"registration_number":"12345678","profession":"study_director","is_involved_in_clinical_trial":true}'
  ```

### Actual result
The page returns 500 error.

### Expected result
The Back-end should return 400 error with the message "Invalid registration number".
The more precise error message should be returned, the better. Best option here is to return 400 error with the message `"Registration number should contain 10 digits"`.
   