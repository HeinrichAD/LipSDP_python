function L = solve_LipSDP(network, lip_params)
    % Solves LipSDP for a given neural network model
    % Handles the three forms of LipSDP: -Neuron, -Network, and -Layer
    % Also handles splitting methods for larger networks
    %
    % params:
    %   * network: struct       - data describing neural network
    %       - fields:
    %           (1) alpha: float            - slope-restricted lower bound
    %           (3) beta: float             - slope-restricted upper bound
    %           (3) net_dims: list of ints  - dimensions of NN
    %           (4) weight_path: str        - path of saved weights of NN
    %   * lip_params: struct    - parameters for LipSDP
    %       - fields:
    %           (1) formulation: str    - LipSDP formulation to use
    %           (2) split: logical      - if true, use splitting 
    %           (3) parallel: logical   - if true, parallelize splitting
    %           (4) verbose: logical    - if true, print CVX output
    %           (5) split_size: int     - size of subnetwork for splitting
    %           (6) num_neurons: int    - number of neurons to couple in
    %                                     LipSDP-Neuron-rand mode
    %           (7) num_workers: int    - number of workers for parallel-
    %                                     ization of splitting formulations
    %
    % returns:
    %   * L: float - computed Lipschitz constant for neural network
    % ---------------------------------------------------------------------
    
    addpath('weight_utils');
    
    % load weights from file
    weights = create_weights(network.net_dims, 'rand');
    
    % if splitting flag is supplied, split network into subnetworks
    if lip_params.split
                
        [split_W, split_net_dims] = split_weights(weights, network.net_dims, ...
            lip_params.split_size);
        L = split_and_solve(split_W, split_net_dims, lip_params, network);
    
    % otherwise, solve a single SDP for the entire network
    else
        
        L = lipschitz_multi_layer(weights, lip_params.formulation, ...
            lip_params.verbose, lip_params.num_neurons, network.net_dims, network);
        
    end
    

end
