import chess
import random
import chess.engine

# Evaluation function for the board (simplified)
def evaluate_board(board):
    material_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0  
    }
    
    score = 0
    for piece in board.piece_map().values():
        piece_value = material_values.get(piece.piece_type, 0)
        if piece.color == chess.WHITE:
            score += piece_value
        else:
            score -= piece_value
    
    return score

def generate_moves(board):
    return list(board.legal_moves)

# Perform a one-step lookahead using beam search
def beam_search(board, beam_width, depth_limit):
    moves = generate_moves(board)
    # Create a list to store possible states (move + evaluation)
    board_evaluations = []
    
    for move in moves:
        board.push(move)
        evaluation = evaluate_board(board)
        board_evaluations.append((move, evaluation))
        board.pop()
    
    # Sort the moves by evaluation and keep only the top beam_width moves
    board_evaluations.sort(key=lambda x: x[1], reverse=True)
    best_moves = [move for move, _ in board_evaluations[:beam_width]]
    
    # Search deeper for the selected best moves
    best_move_sequence = []
    best_score = -float('inf')
    
    for move in best_moves:
        board.push(move)
        move_sequence, score = search_depth(board, beam_width, depth_limit - 1)
        board.pop()
        
        if score > best_score:
            best_score = score
            best_move_sequence = [move] + move_sequence
    
    return best_move_sequence, best_score

# Search recursively up to a certain depth using beam search
def search_depth(board, beam_width, depth):
    if depth == 0:
        return [], evaluate_board(board)
    
    # Generate all possible moves
    moves = generate_moves(board)
    board_evaluations = []
    
    for move in moves:
        board.push(move)
        evaluation = evaluate_board(board)
        board_evaluations.append((move, evaluation))
        board.pop()
    
    # Sort the moves by evaluation and keep only the top beam_width moves
    board_evaluations.sort(key=lambda x: x[1], reverse=True)
    best_moves = [move for move, _ in board_evaluations[:beam_width]]
    
    # Recursively evaluate the best moves
    best_move_sequence = []
    best_score = -float('inf')
    
    for move in best_moves:
        board.push(move)
        move_sequence, score = search_depth(board, beam_width, depth - 1)
        board.pop()
        
        if score > best_score:
            best_score = score
            best_move_sequence = [move] + move_sequence
    
    return best_move_sequence, best_score

# Main function to predict the best move
def predict_best_move(board, beam_width=3, depth_limit=3):
    best_move_sequence, best_score = beam_search(board, beam_width, depth_limit)
    return best_move_sequence[0], best_score  # Return the best move and its evaluation

# Initialize chess board
board = chess.Board()

# Predict the best move using beam search
best_move, best_score = predict_best_move(board, beam_width=3, depth_limit=3)

# Display the best move and its evaluation score
print("Best Move:", best_move)
print("Best Move Evaluation:", best_score)

# Visualize the board
print(board)
