require "open-uri"
require "nokogiri"

def fetch(url="")
    open("https://en.wikipedia.org/wiki/Douglas_Adams") do |html|
        response = Nokogiri::HTML(html)
        return { data: response }
    end
end