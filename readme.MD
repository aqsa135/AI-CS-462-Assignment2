### Assignment 2: Search and Learning
#### Due Friday 9/22 at the start of class. 

Note: For the programming  portions of the assignment, please provide a file called submission.py that demos your code.

**Question 1. (20 points)**

Fill in the following table. (you're more than welcome to recreate this in a separate document)

| Algorithm  | Time Complexity                      | Space Complexity          | Complete?                                                                                        | Optimal?                                         |
|---|--------------------------------------|---------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------|
| BFS  | exponential-time, requiring O(b^d+1) | exponential spaceO(b^d+1) | Yes                                                                                              | Yes, assuming that all actions have uniform cost |
| UCS  | exponential O(b^(1+C/ε))             | O((b^(d+1))               | yes                                                                                              | yes                                              |
| DFS   | exponential time O(b^n)              | linear (O(bn)) space      | Yes on a finite grpah, no on if space is infinitely large and we can't check for repeated states | No                                               |
| DLS  | O(b^1)                               | O(b1)                     | No                                                                                               | No                                               |
| IDS | O(b^d)                               | O(bd)                     | Yes                                                                                              | Yes                                              |
|A*  | O(b^d)                               | O(b^d)                    | Yes                                                                                              | Yes                                              |

**Question 2** 

Our Mars Rover needs to collect some soil samples. It has three hoppers to hold these samples. Unfortunately, during the landing, the markings on the hoppers were burned off, so our agent only knows how much each hopper holds. (careful observers may note the resemblance to the Water Jug problem.)

Luckily, our agent has access to some search algorithms that it can use. Using VacuumState as an example, you will need to complete the implementation of the HopperState class so that our rover can solve the problem.

a) (5 points) To begin, we need to implement the eq, hash, and lt methods in the HopperState class in order for the closed list and priority queue to function correctly. (You should use cost as the way to compare states. Implement unit tests in a file called test_HopperState.py that allow you to determine that these methods are working correctly.

b) (10 points) Next, implement successors. For any state, our robot has the following actions:

    It can fill any of the three hoppers. This will result in them being completely full.
    It can dump out any of the three hoppers. This will result in that hopper being empty.
    It can pour soil from hopper A to hopper B. This will have one of two outcomes:
        Hopper A is empty, and hopper B contains all the soil from both hoppers.
        Hopper B is full, and some leftover soil remains in hopper A.

successors should return a list of successor states. 
You do not need to generate states that result in no change. (for example, dumping out an empty bucket.) 
Implement a unit test in test_HopperState that allows you to confirm that successor is working correctly. 

Note: good coding practices are encouraged here. 
If you find yourself creating complex loops or nested if/else's, refactor.

c) (5 points) Now let's try it out on the given algorithms. I've provided BFS and DFS implementations for you. Run this problem with the following three goals using both BFS and DFS, assuming the hoppers start empty. (Don't do the hard one until you're sure the closed list is working correctly.)

    Easy: [5 0 0]
    Medium: [4 0 0]
    Hard: [4 4 0]

Adapt the code to print out the number of states generated at the end.

d) (10 points) Last, note that DFS has a limit parameter that is not used. Extend DFS to only add new nodes to the search queue if they have cost < limit. This will implement DLS for us. Then, write a method called IterativeDeepeningSearch - this should just be a loop that calls DLS with increasing limits until the solution is found.

e) (5 points) Please include a table that shows how many states were generated for each of the problems (Easy, Medium, Hard) for BFS, DFS, DLS, and IDS.

| Algorithm                           | Number of States | States Generated |
|-------------------------------------|:----------------:|:----------------:|
| Breadth-First Search (BFS)          | 900              | 143              |
| Depth-First Search (DFS)            | 1813             | 160              |
| Depth-Limited Search (DLS) (Lim=10) | 1938             | 64               |
| Iterative Deepening Search (IDS)    | 2749            | 34               |


**Question 3** 

For this problem, we will need for our rover to find its way from the sample site back to the charger. Fortunately, we have a map that we can use to find our way. There's a picture of it in the marsmap.docx file; the red cells are areas we cannot travel in.

This data is also captured in the MarsMap file.

You will need to:

a) (5 points) Complete the read_mars_graph() method so that you can create a graph. I've provided a Graph class for you; if you want to modify it, feel free. You may want to look at RomaniaGraph to get some ideas.

b) (15 points) In SearchAlgorithms.py, complete the a_star function. You will need to implement a straight-line distance heuristic. This should compute SLD(p1, p2) = sqrt((p1.x - p2.x)^2 + (p1.y - p2.y)^2))

SLD should be a separate function that is provided to a_star, NOT something encoded within the algorithm. You should be able to pass in a different heuristic function, 
such as h1, which always returns 0, without changing your code.

c) (5 points) Run both A* and uniform cost search (i.e. using h1: h=0 for all states) on the MarsMap and count the number of states generated. Add this to your results.

**Question 4**

In this question, you'll get some practice working with scikit-learn. 
You'll see how to set up a supervised learning problem, evaluate an algorithm, and manage training and test sets.

We'll work with the code in sklearn_intro.py.

To begin, take a look at ZeroR. We will use this throughout the course as a *default* learning rule. 
That is, when we don't know what else to do, we'll fall back on ZeroR as a last resort and choose 
the most common classification.

This is fine, but it has one weakness - it only makes errors of one type. That is, if we are dealing with the breast cancer data, it will get all "no-recurrence-events" examples right, and all "recurrence-events" examples wrong.
Our accuracy over the entire dataset will still be (on average) as good as we can expect, but we might prefer to also distribute our errors across the different classes.

In this case, we'll use a slightly different default: RandR. RandR returns one of the classifications at random, with a probability equal to its frequency in the training set.
So, if our dataset is 60% "no-recurrence-events" and 40% "recurrence-events", we should return 'recurrence-events' with p=0.4 and 'no-recurrence-events'
 with p=0.6.

Luckily, there's an easy way to do this, which is to randomly select an element from the training set and return its classification. 

a) (5 points) Implement RandR. 

b) (5 points) As we discussed in class, it's important to separate our data into training and test sets. In sklearn_intro, I show you how to load in the Iris dataset and split the data with sklearn. 
I would like you to also implement the split into test and training sets by hand.  

c) (10 points) Lastly, I would like you to implement five-fold cross-validation by hand. I show you how to do it with sklearn; your code should break the dataset into five folds, 
repeatedly train on 4 and test on the fifth fold, and compute the accuracy across all five folds using RandR and ZeroR.


**Question 5: (grad students only)**

A problem that computer scientists and biologists have been working on for almost 50 years is the [protein folding problem](https://www.youtube.com/watch?v=KpedmJdrTpY).

It's a huge combinatorial search problem that was traditionally tackled using techniques like the ones we've 
been studying. 

Recently, researchers at DeepMind have developed a new approach to this problem, called [AlphaFold](https://www.deepmind.com/research/highlighted-research/alphafold), which 
employs machine learning to attack the problem differently. In a nutshell, a neural network is used to learn a 
highly accurate evaluation function. This greatly reduces the size of the space that needs to be searched, allowing 
AlphaFold to identify almost any protein structure. 

Please take a look at the site linked above, watch the videos and read their descriptions, and prepare a short (2-3 paragraph)
response that answers the following questions:
- Why is the protein folding problem so hard?
- What is CASP?
- How does AlphaFold enable scientific discovery? What's an example of a problem it's
been used to solve?

