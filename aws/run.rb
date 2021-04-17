require_relative "src/fetch.rb"

def scrape(event:, context:)
    @data = fetch
    { success: true, data: @data }
end

if __FILE__ == $0
    p scrape event: nil, context: nil
end