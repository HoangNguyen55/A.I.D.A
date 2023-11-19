use reqwest::blocking::Client;
use scraper::{Html, Selector};
//use std::fs::File;
//use std::io::{stdin,stdout,Write};
use clap::Parser;


#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Valid: -url or -html
    #[arg(short, long)]
    output: String,

    /// Valid: -e or -o
    #[arg(short, long)]
    engine: String,

    /// Valid: any string
    #[arg(short, long)]
    s: String,

    
}


fn main() -> Result<(), Box<dyn std::error::Error>> 
{ 
    //CMD LINE CONVERSION (Rust Syntax)

    let args = Args::parse();
 
    println!("Command Input: {}", args.output);
    println!("Command Input: {}", args.engine);
    println!("Command Input: {}", args.s);

    ////TERMINAL INPUT (FOR TESTING)
    //let mut s=String::new();
    //print!("Enter Search: ");
    //let _=stdout().flush();
    //stdin().read_line(&mut s).expect("Did not enter a correct string");
    //if let Some('\n')=s.chars().next_back() {
    //    s.pop();
    //}
    //if let Some('\r')=s.chars().next_back() {
    //    s.pop();
    //}
//
    let client = Client::new();
    //let query = "warframe+guide";
    let query = args.s.replace("_", "+");
    println!("Query Dump into program: {}", query);
    let url = format!("https:www.google.com/search?q={}" , query);
    let res = client.get(&url).header(reqwest::header::USER_AGENT, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36").send()?;
    let html = res.text()?;
    let fragment = Html::parse_document(&html);
    let selector = Selector::parse("div.g")?;


    let ui_friendly_query_print = query.replace("+", " ");
    println!("Showing Results For: {}", ui_friendly_query_print);
    println!("\n");
    let mut resarray = Vec::new();
    let mut resultcount = 0;
    for element in fragment.select(&selector) {
        if resultcount < 5 {
            let title_selector = Selector::parse("h3")?;
            let title_element = element.select(&title_selector).next().ok_or("ERROR: Title Element not Found")?;
            let title = title_element.text().collect::<Vec<_>>().join("");

            let link_selector = Selector::parse("a[href]")?;
            let link_element = element.select(&link_selector).next().ok_or("ERROR: Link Element not Found")?;
            let link = link_element.value().attr("href").ok_or("ERROR: href Attribute not Found")?;

            let snippet_selector = Selector::parse(".VwiC3b")?;
            let snippet_element = match element.select(&snippet_selector).next(){
                None => "ERROR: Snippet Element not Found".to_string(),
                Some(snippet) => snippet.text().collect::<Vec<_>>().join(""),
            };

            println!("Title: {}", title);
            println!("Link: {}", link);
            println!("Snippet: {}", snippet_element);
        
            println!("\n");
            resarray.push(link.to_string());
            resultcount += 1;
        }
        else{
            break;
        }
    }
    for x in &resarray{
        println!("Link Path: {:?}", x);
    }

    ////USE THIS TO DEBUG HTML QUERY RESULT
    //let mut file = File::create("debugoutput.html")?;
    //writeln!(file, "Output: {}", html)?;

    //println!("Raw HTML written to file.");
    //println!("Output: {}", html);
    Ok(())
}