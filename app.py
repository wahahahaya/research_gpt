import arxiv

id = input("Please input the id of the paper: ")
# search engine
client = arxiv.Client()
search = arxiv.Search(id_list=[id])

# extract and show the result
paper = next(search.results())

# install paper to icloud
paper.download_pdf(dirpath="/Users/Arlen/Desktop/paper", filename=paper.title + ".pdf")

# write the result into summary.md
filename = "/Users/Arlen/Vscode/gpt_paper/summary.md"
with open(filename, "a", encoding="utf-8") as file:
    file.write("# " + paper.title + "\n")
    file.write("Published in " + paper.published.strftime("%m/%d/%Y, %H:%M:%S") + "\n")
    file.write("url " + paper.entry_id + "\n")
    file.write("## Summary\n")
    file.write("- " + paper.summary + "\n\n")
