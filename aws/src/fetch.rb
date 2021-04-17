require "open-uri"
#require "nokogiri"

def fetch(url="https://www.amazon.co.uk/gp/product/B08KWJ9YND/")
    start = Time.new
    open(url, "User-Agent" => "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0") do |resp|
        #response = Nokogiri::HTML resp.read

        #p response
        p resp.read
        return { time: Time.new - start }
    end
end