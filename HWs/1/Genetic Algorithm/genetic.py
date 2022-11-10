from typing import Tuple
import numpy as np
import pandas as pd
from tqdm import tqdm


class Genetic:

    """
    NOTE:
        - S is the set of members.
        - T is the target value.
        - Chromosomes are represented as an array of 0 and 1 with the same length as the set.
        (0 means the member is not included in the subset, 1 means the member is included in the subset)

        Feel free to add any other function you need.
    """

    def __init__(self):
        pass

    def generate_initial_population(self, n: int, k: int) -> np.ndarray:
        """
        Generate initial population: This function is used to generate the initial population.

        Inputs:
        - n: number of chromosomes in the population
        - k: number of genes in each chromosome

        It must generate a population of size n for a set of k members.

        Outputs:
        - initial population
        """

        pass

    def objective_function(self, chromosome: np.ndarray, S: np.ndarray) -> int:
        """
        Objective function: This function is used to calculate the sum of the chromosome.

        Inputs:
        - chromosome: chromosome to be evaluated
        - S: set of members

        It must calculate the sum of the members included in the subset (i.e. sum of S[i]s where Chromosome[i] == 1).

        Outputs:
        - sum of the chromosome
        """

        pass

    def is_feasible(self, chromosome: np.ndarray, S: np.ndarray, T: int) -> bool:
        """
        This function is used to check if the sum of the chromosome (objective function) is equal or less to the target value.

        Inputs:
        - chromosome: chromosome to be evaluated
        - S: set of members
        - T: target value

        Outputs:
        - True (1) if the sum of the chromosome is equal or less to the target value, False (0) otherwise
        """

        pass

    def cost_function(self, chromosome: np.ndarray, S: np.ndarray, T: int) -> int:
        """
        Cost function: This function is used to calculate the cost of the chromosome.

        Inputs:
        - chromosome: chromosome to be evaluated
        - S: set of members
        - T: target value

        The cost is calculated in this way:
        - If the chromosome is feasible, the cost is equal to (target value - sum of the chromosome)
        - If the chromosome is not feasible, the cost is equal to the sum of the chromosome

        Outputs:
        - cost of the chromosome
        """

        pass

    def selection(self, population: np.ndarray, S: np.ndarray, T: int) -> Tuple[np.ndarray, np.ndarray]:
        """
        Selection: This function is used to select the best chromosome from the population.

        Inputs:
        - population: current population
        - S: set of members
        - T: target value

        It select the best chromosomes in this way:
        - It gets 4 random chromosomes from the population
        - It calculates the cost of each selected chromosome
        - It selects the chromosome with the lowest cost from the first two selected chromosomes
        - It selects the chromosome with the lowest cost from the last two selected chromosomes
        - It returns the selected chromosomes from two previous steps

        Outputs:
        - two best chromosomes with the lowest cost out of four selected chromosomes
        """

        pass

    def crossover(self, parent1: np.ndarray, parent2: np.ndarray, S: np.ndarray, prob: float = 0.5) -> Tuple[np.ndarray, np.ndarray]:
        """
        Crossover: This function is used to create two new chromosomes from two parents.

        Inputs:
        - parent1: first parent chromosome
        - parent2: second parent chromosome


        It creates two new chromosomes in this way:
        - It gets a random number between 0 and 1
        - If the random number is less than the crossover probability, it performs the crossover, otherwise it returns the parents
        - Crossover steps:
        -   It gets a random number between 0 and the length of the parents
        -   It creates two new chromosomes by swapping the first part of the first parent with the first part of the second parent and vice versa
        -   It returns the two new chromosomes as children


        Outputs:
        - two children chromosomes
        """

        pass

    def mutation(self, child1: np.ndarray, child2: np.ndarray, prob: float = 0.01) -> Tuple[np.ndarray, np.ndarray]:
        """
        Mutation: This function is used to mutate the child chromosomes.

        Inputs:
        - child1: first child chromosome
        - child2: second child chromosome
        - prob: mutation probability

        It mutates the child chromosomes in this way:
        - It gets a random number between 0 and 1
        - If the random number is less than the mutation probability, it performs the mutation, otherwise it returns the children
        - Mutation steps:
        -   It gets a random number between 0 and the length of the children
        -   It mutates the first child by swapping the value of the random index of the first child
        -   It mutates the second child by swapping the value of the random index of the second child
        -   It returns the two mutated children

        Outputs:
        - two mutated children chromosomes
        """

        pass

    def run_algorithm(self, S: np.ndarray, T: int, crossover_probability: float = 0.5, mutation_probability: float = 0.1, population_size: int = 100, num_generations: int = 100):
        """
        Run algorithm: This function is used to run the genetic algorithm.

        Inputs:
        - S: array of integers
        - T: target value

        It runs the genetic algorithm in this way:
        - It generates the initial population
        - It iterates for the number of generations
        - For each generation, it makes a new empty population
        -   While the size of the new population is less than the initial population size do the following:
        -       It selects the best chromosomes(parents) from the population
        -       It performs the crossover on the best chromosomes
        -       It performs the mutation on the children chromosomes
        -       If the children chromosomes have a lower cost than the parents, add them to the new population, otherwise add the parents to the new population
        -   Update the best cost if the best chromosome in the population has a lower cost than the current best cost
        -   Update the best solution if the best chromosome in the population has a lower cost than the current best solution
        -   Append the current best cost and current best solution to the records list
        -   Update the population with the new population
        - Return the best cost, best solution and records


        Outputs:
        - best cost
        - best solution
        - records
        """

        # UPDATE THESE VARIABLES (best_cost, best_solution, records)
        best_cost = np.Inf
        best_solution = None
        records = []

        # YOUR CODE HERE

        for i in tqdm(range(num_generations)):

            # YOUR CODE HERE
            pass

            records.append({'iteration': i, 'best_cost': best_cost,
                           'best_solution': best_solution})  # DO NOT REMOVE THIS LINE

        records = pd.DataFrame(records)  # DO NOT REMOVE THIS LINE

        return best_cost, best_solution, records
