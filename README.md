# NYC_Graph_network

[New York Social Diary](https://www.newyorksocialdiary.com/category/party-pictures/) provides a fascinating lens onto New York's socially well-to-do. The data forms a natural social graph for New York's social elite. 

In this website, the photos have carefully annotated captions labeling those that appear in the photos. We can think of this as implicitly implying a social graph: there is a connection between two individuals if they appear in a picture together.

In this project, I assembled the social graph from photo captions for parties dated from 2007-2015. Using this graph, it is likely to guesses at the most popular socialites, the most influential people, and the most tightly coupled pairs.

More detail of how the code work can be found in `project_details.pdf`

## Step 1: Get a list of all the photo pages to be analyzed. Then parse all of the captions on all page
- Run `caption_scraper_and_parser.py`

## Step 2: Assemble the graph
- Run `event_freq.py`
- Run `NYC_graph.py`
- Run `graph_analysis.py`
It will output the network graph, top 100 popular people, and top 100 best friend.

