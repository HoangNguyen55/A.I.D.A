use reqwest::blocking::Client;
use scraper::{Html, Selector};

fn main() -> Result<(), Box<dyn std::error::Error>> 
{ 
 let client = Client::new(); 
 let query = "rust+programming+language";
 let url = format!("https:www.google.com/search?q={}" , query);
 let res = client.get(&url).send()?;
 let html = res.text()?;
 let fragment = Html::parse_document(&html);
 let selector = Selector::parse("div.g").unwrap();

 for element in fragment.select(&selector) {
    let title_selector = Selector::parse("h3").unwrap();
    let title_element = element.select(&title_selector).next().unwrap();
    let title = title_element.text().collect::<Vec<_>>().join("");

    let link_selector = Selector::parse(".yuRUbf > a").unwrap();
    let link_element = element.select(&link_selector).next().unwrap();
    let link = link_element.value().attr("href").unwrap();

    let snippet_selector = Selector::parse(".VwiC3b").unwrap();
    let snippet_element = element.select(&snippet_selector).next().unwrap();
    let snippet = snippet_element.text().collect::<Vec<_>>().join("");

    println!("Title: {}", title);
    println!("Link: {}", link);
    println!("Snippet: {}", snippet);
}
println!("Output: {}", html);
Ok(())
}