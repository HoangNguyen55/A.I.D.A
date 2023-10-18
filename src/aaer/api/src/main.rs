use reqwest::blocking::Client;
use scraper::{Html, Selector};
use std::fs::File;
use std::io::Write;


fn main() -> Result<(), Box<dyn std::error::Error>> 
{ 
    let client = Client::new(); 
    let query = "warframe+guide";
    let url = format!("https:www.google.com/search?q={}" , query);
    let res = client.get(&url).header(reqwest::header::USER_AGENT, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36").send()?;
    let html = res.text()?;
    let fragment = Html::parse_document(&html);
    let selector = Selector::parse("div.g")?;

    let ui_friendly_query_print = query.replace("+", " ");
    println!("Search Query: {}", ui_friendly_query_print);
    println!("\n");
    for element in fragment.select(&selector) {
        let title_selector = Selector::parse("h3")?;
        let title_element = element.select(&title_selector).next().ok_or("ERROR: Title Element not Found")?;
        let title = title_element.text().collect::<Vec<_>>().join("");

        let link_selector = Selector::parse(".yuRUbf")?;
        let link_element = element.select(&link_selector).next().ok_or("ERROR: Link Element not Found")?;
        //let link = link_element.value().attr("href").ok_or("ERROR: href Attribute not Found")?;

        let snippet_selector = Selector::parse(".VwiC3b")?;
        let snippet_element = element.select(&snippet_selector).next().ok_or("ERROR: Snippet Element not Found")?;
        let snippet = snippet_element.text().collect::<Vec<_>>().join("");

        println!("Title: {}", title);
        //println!("Link: {}", link);
        println!("Snippet: {}", snippet);
        println!("\n");
    }
    let mut file = File::create("debugoutput.html")?;
    writeln!(file, "Output: {}", html)?;

    println!("Raw HTML written to file.");
    //println!("Output: {}", html);
    Ok(())
}