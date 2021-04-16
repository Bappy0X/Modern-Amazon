> "Serverless" scraping for Amazon data - using AWS Lambda

Built with Ruby - I promise I'm *not* insane...

Set up with serverless framework, this makes everything easier and doesn't have to be set up entirely manually.

### The data that we want:

- ASIN
- Title
- Image(s)
- Buy-Box Price
- Delivery times? (May be difficult due to locations etc)
- Reviews
    - Amount of ratings
    - Average rating
- Categories
    - Best Sellers Rank
- Dimensions

From:

- A list of products (Example, https://www.amazon.co.uk/gcx/Gifts-for-Everyone/gfhz/)
- A single product (Example, https://smile.amazon.co.uk/dp/1509868089/)

### File Structure

- src/
    
    The containing folder of our actual code

    - [/src/fetch.rb](fetch.rb)

- [run.rb](run.rb)

    The file that will enclose all the code needed for running the Lambda function itself, and will reference the src code inside

- [serverless.yml](serverless.yml)

    This is the file used for describing the structure the of our AWS Lambda - this is powered by [Serverless Framework](https://www.serverless.com/)

> Gonna take a break to watch a movie (L4yer Cak3) and think...