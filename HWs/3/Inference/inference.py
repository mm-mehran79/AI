class BN(object):
    """
    Bayesian Network implementation with sampling methods as a class
    
    Attributes
    ----------
    n: int
        number of variables
        
    G: dict
        Network representation as a dictionary. 
        {variable:[[children],[parents]]} # You can represent the network in other ways. This is only a suggestion.

    topological order: list
        topological order of the nodes of the graph

    CPT: list
        CPT Table
    """
    
    def __init__(self) -> None:
        ############################################################
        # Initialzie Bayesian Network                              #
        # (1 Points)                                               #
        ############################################################
        
        #Your code
        pass
    
    def cpt(self, node, value) -> dict:
        """
        This is a function that returns cpt of the given node
        
        Parameters
        ----------
        node:
            a variable in the bayes' net
            
        Returns
        -------
        result: dict
            {value1:{{parent1:p1_value1, parent2:p2_value1, ...}: prob1, ...}, value2: ...}
        """
        ############################################################
        # (3 Points)                                               #
        ############################################################
        
        #Your code
        pass
    
    def pmf(self, query, evidence) -> float:
        """
        This function gets a variable and its value as query and a list of evidences and returns probability mass function P(Q=q|E=e)
        
        Parameters
        ----------
        query:
            a variable and its value
            e.g. ('a', 1)
        evidence:
            list of variables and their values
            e.g. [('b', 0), ('c', 1)]
        
        Returns
        -------
        PMF: float
            P(query|evidence)
        """
        ############################################################
        # (3 Points)                                               #
        ############################################################
        
        #Your code
        pass
    
    def sampling(self, query, evidence, sampling_method, num_iter, num_burnin = 1e2) -> float:
        """
        Parameters
        ----------
        query: list
            list of variables an their values
            e.g. [('a', 0), ('e', 1)]
        evidence: list
            list of observed variables and their values
            e.g. [('b', 0), ('c', 1)]
        sampling_method:
            "Prior", "Rejection", "Likelihood Weighting", "Gibbs"
        num_iter:
            number of the generated samples 
        num_burnin:
            (used only in gibbs sampling) number of samples that we ignore at the start for gibbs method to converge
            
        Returns
        -------
        probability: float
            approximate P(query|evidence) calculated by sampling
        """
        ############################################################
        # (27 Points)                                              #
        #     Prior sampling (6 points)                            #
        #     Rejection sampling (6 points)                        #
        #     Likelihood weighting (7 points)                      #
        #     Gibbs sampling (8 points)                      #
        ############################################################
        
        #Your code
        pass


    def prior_sample(self, query, evidence, num_iter):
        """
            Parameters
            ----------
            query:
                query set
            evidence:
                evidence set
            num_iter:
                number of genereted samples

            Returns
            -------
            prior samples
        """
        pass
        
        
    def sample_consistent_with_evidence(self, sample, evidence):
        """
            To check if a sample is consistent with evidence or not?

            Parameters
            ----------
            sample:
                a sample
            evidence:
                evidence set
            
            Returns
            -------
            True if the sample is consistent with evidence, False otherwise.
        """
        pass
    
    
    def sample_consistent_with_query(self, sample, query):
        """
            To check a sample is consistent with query or not?

            Parameters
            ----------
            sample:
                a sample
            evidence:
                query set
            
            Returns
            -------
            True if the sample is consistent with query, False otherwise.
        """
        pass
        
        
    def get_prior_sample(self):
        """
            Returns
            -------
            Returns a set which is the prior sample. 
        """
        pass
    
    
    def rejection_sample(self, query, evidence, num_iter):
        """
            Parameters
            ----------
            query:
                query set
            evidence:
                evidence set
            num_iter:
                number of genereted samples

            Returns
            -------
            rejection samples
        """
        pass
    
    
    def likelihood_sample(self, query, evidence, num_iter):
        """
            Parameters
            ----------
            query:
                query set
            evidence:
                evidence set
            num_iter:
                number of genereted samples

            Returns
            -------
            likelihood samples
        """
        pass
            
        
    def gibbs_sample(self, query, evidence, num_iter, num_burnin):
        """
            Parameters
            ----------
            query:
                query set
            evidence:
                evidence set
            num_iter:
                number of genereted samples

            Returns
            -------
            gibbs samples
        """
        pass
    
    
    def topological_sort(self, node, visited):
        """
            This function wants to make a topological sort of the graph and set the topological_order parameter of the class.

            Parameters
            ----------
            node:
                the list of nodes
            visited:
                the list of visited(1)/not visited(0) nodes

        """
        pass

    def set_topological_order(self):
        """
            This function calls topological sort function and set the topological sort.
        """
        pass   
            
    def all_parents_visited(self, node, visited) -> bool:
        """
            This function checks if all parents are visited or not?

            Parameters
            ----------
            node:
                the list of nodes
            visited:
                the list of visited(1)/not visited(0) nodes

            Return
            ----------
            return True if all parents of node are visited, False otherwise.
        """
        pass
           
        
    def remove_nonmatching_evidences(self, evidence, factors):
        pass
               
            
    def join_and_eliminate(self, var, factors, evidence):
        pass
        
        
    def get_joined_factor(self, var_factors, var, evidence):
        pass
    
    
    def get_rows_factor(self, factor, var, evidence, values, variables_in_joined_factor):
        pass
    
        
    def get_var_factors(self, var, factors):
        pass
             
        
    def get_variables_in_joined_factor(self, var_factors, var, evidence):
        pass
    
    
    def get_join_all_factors(self, factors, query, evidence):
        pass
    
    
    def get_row_factor(self, factor, query_vars, evidence, values):
        pass
    
    
    def normalize(self, joint_factor):
        pass