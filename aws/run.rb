require_relative "src/fetch.rb"

def scrape(event:, context:)
    p fetch
    { success: true, data: ["one", "two", "three"] }
end

scrape event: nil, context: nil