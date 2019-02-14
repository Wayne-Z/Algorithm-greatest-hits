# Algorithm-greatest-hits

A collection of the greatest hits from the world of algorithms.

## Personal collection of algorithms
#### Implemented from scratch in _Python_ (definitely **not** optimized, do not blame me!). The goal of this repo is mostly educational. If you spot any mistakes and/or have any suggestions on how to optimize or refactor some of the code, feel free to contribute or contact me!

## Graph 

* [Traveling Salesman](https://github.com/Zymrael/Algorithm-greatest-hits/blob/master/graph%20algorithms/TSP/TSP.py): Dynamic programming solution for the TSP problem. Finds the optimal tour but is memory intensive and quite slow for graphs with n >= 25.

#### Topology

* [Karger's Min Cut](https://github.com/Zymrael/Algorithm-greatest-hits/tree/master/graph%20algorithms/Karger's%20min%20cut):
  Randomized algorithm to compute the _minimum cut_ in an undirected graph. Implemented on adjacency lists, currently poorly optimized. **O(m^2)** time, **O(m)** space
  
#### Shortest paths

* [Dijkstra's single source shortest paths](https://github.com/Zymrael/Algorithm-greatest-hits/tree/master/graph%20algorithms/Dijkstra):
Perhaps one of the most popular algorithm for the shortest path problem in a non-negative edge graph. This particular implementation does not use **heaps** and runs in **O(n^2)** instead of **O(mn)**

* [Johnson's all pairs shortest paths](https://github.com/Zymrael/Algorithm-greatest-hits/blob/master/graph%20algorithms/Johnson's%20APSP/Johnson's.py): Classic algorithm for the all-pairs shortest paths in a directed graph. Uses a round of Bellman Ford's single source shortest path algorithm to find a reweighted version of the original graph without negative edges, and subsequently runs Dijkstra's **n** times. Time complexity depends on the particular implementation of Dijkstra and Bellman Ford

**Optimizations**: This particular Bellman Ford implementation uses the standard dynamic programming space optimization technique of remembering only the needed inputs for the recurrence.

#### Minimum Spanning Tree

* [Prim's minimum spanning tree](https://github.com/Zymrael/Algorithm-greatest-hits/tree/master/graph%20algorithms/Prim's%20MST):

## Sorting

* [Merge Sort](https://github.com/Zymrael/Algorithm-greatest-hits/blob/master/sorting/MergeSort.py): Vanilla implementation of the basic _divide and conquer_ sorting algorithm. **O(n log n)** time, **O(n)** space 

* [Quick Sort](https://github.com/Zymrael/Algorithm-greatest-hits/blob/master/sorting/QuickSort.py): Randomized, in-place quick sort. **O(n log n)** time, **O(1)** space  

## Mixed -- practice problems

* [Karatsuba's multiplication](https://github.com/Zymrael/Algorithm-greatest-hits/blob/master/math/Karatsuba%20mult.py): A faster way to multiply two numbers 

* [2Sum](https://github.com/Zymrael/Algorithm-greatest-hits/blob/master/mixed/2SUM/2SUM.py): Finding two numbers such that their sum is equal to a certain target.

* [Heap Median](https://github.com/Zymrael/Algorithm-greatest-hits/blob/master/mixed/heapMedian/median_maintenance.py): Running median maintenance with double heap.

* [Scheduling](https://github.com/Zymrael/Algorithm-greatest-hits/tree/master/mixed/Scheduling): Various simple greedy algorithms for job scheduling
