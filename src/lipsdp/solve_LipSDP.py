from . import lipschitz_multi_layer
from . import split_and_solve
from . import weight_utils


def solve_LipSDP(network, lip_params):
    # Solves LipSDP for a given neural network model
    # Handles the three forms of LipSDP: -Neuron, -Network, and -Layer
    # Also handles splitting methods for larger networks
    #
    # params:
    #   * network: dictionary       - data describing neural network
    #       - keys:
    #           (1) alpha: float            - slope-restricted lower bound
    #           (2) beta: float             - slope-restricted upper bound
    #           (3) weights: list           - loaded weights of neural network
    #           (4) net_dims: list of ints  - dimensions of each layer in network
    #   * lip_params: struct        - parameters for LipSDP
    #       - fields:
    #           (1) formulation: str      - LipSDP formulation to use
    #           (2) split: logical        - if true, use splitting
    #           (3) parallel: logical     - if true, parallelize splitting
    #           (4) verbose: logical      - if true, print CVX output
    #           (5) split_size: int       - size of subnetwork for splitting
    #           (6) num_neurons: int      - number of neurons to couple in
    #                                       LipSDP-Neuron-rand mode
    #           (7) num_workers: int      - number of workers for parallel-
    #                                       ization of splitting formulations
    #           (8) solver: str, optional - solver to use
    #
    # returns:
    #   * L: float - computed Lipschitz constant for neural network
    # ---------------------------------------------------------------------

    # if splitting flag is supplied, split network into subnetworks
    if lip_params['split']:

        split_W, split_net_dims = weight_utils.split_weights(
            network['weights'], network['net_dims'], lip_params['split_size'])
        L = split_and_solve.split_and_solve(split_W, split_net_dims, lip_params, network, lip_params['solver'])

    # otherwise, solve a single SDP for the entire network
    else:

        L = lipschitz_multi_layer.lipschitz_multi_layer(
            network['weights'], lip_params['formulation'], lip_params['verbose'],
            lip_params['num_neurons'], lip_params['num_dec_vars'],
            network['net_dims'], network, lip_params['solver'])

    return L
