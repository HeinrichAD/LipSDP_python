from enum import Enum
import numpy as np
from typing import List

from .solve_LipSDP import solve_LipSDP


class LipSDP():

    class Formulation(Enum):
        """
        LipSDP formulation.
        """
        NEURON = "neuron"
        NETWORK = "network"
        LAYER = "layer"
        NETWORK_RAND = "network-rand"
        NETWORK_DEC_VARS = "network-dec-vars"

        def __str__(self):
            return self.value

    class NetworkOptions:

        def __init__(
            self,
            weights: np.ndarray,
            net_dims: List[int],
            alpha: float = 0,
            beta: float = 1,
        ) -> None:
            """
            Initialize LipSDP network options.

            Args:
                weights (np.ndarray): Weights of neural network.
                net_dims (List[int]): Dimensions of each layer in network
                alpha (float, optional): Lower bound for slope restriction bound. Defaults to 0.
                beta (float, optional): Lower bound for slope restriction bound. Defaults to 1.
            """
            self.weights = weights
            self.net_dims = net_dims
            self.alpha = alpha
            self.beta = beta

    class LipParams:

        def __init__(
            self,
            formulation: "LipSDP.Formulation" = "neuron",
            verbose: bool = False,
            num_neurons: int = 100,
            split: bool = False,
            parallel: bool = False,
            split_size: int = 2,
            num_workers: int = 0,
            num_dec_vars: int = 10,
            solver: str = "CVXOPT",
        ) -> None:
            """
            LipSDP options.

            Args:
                formulation (LipSDP.Formulation, optional): LipSDP formulation to use. Defaults to "neuron".
                verbose (bool, optional): Prints CVX output from solve if supplied. Defaults to False.
                num_neurons (int, optional): Number of neurons to couple for LipSDP-Network-rand formulation. Defaults to 100.
                split (bool, optional): Splits network into subnetworks for more efficient solving if supplied. Defaults to False.
                parallel (bool, optional): Parallelizes solving for split formulations if supplied. Defaults to False.
                split_size (int, optional): Number of layers in each subnetwork for splitting formulations. Defaults to 2.
                num_workers (int, optional): Number of workers for parallelization of splitting formulations. Defaults to 0.
                num_dec_vars (int, optional): Specify number of decision variables to be used for LipSDP. Defaults to 10.
                solver (str, optional): Solver to use. Defaults to "CVXOPT".

            Raises:
                ValueError: When you use parallel, num_workers must be an integer >= 1.
                ValueError: When you use split, split_size must be an integer >= 1.
            """
            self.formulation = formulation
            self.verbose = verbose
            self.num_neurons = num_neurons
            self.split = split
            self.parallel = parallel
            self.split_size = split_size
            self.num_workers = num_workers
            self.num_dec_vars = num_dec_vars
            self.solver = solver

            if self.parallel is True and self.num_workers < 1:
                raise ValueError("When you use parallel, num_workers must be an integer >= 1.")
            if self.split is True and self.split_size < 1:
                raise ValueError("When you use split, split_size must be an integer >= 1.")

    def __init__(self, network: NetworkOptions, lip_params: LipParams) -> None:
        self.network = network
        self.lip_params = lip_params

    def solve(self) -> float:
        return solve_LipSDP(self.network.__dict__, self.lip_params.__dict__)
