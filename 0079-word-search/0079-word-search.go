func exist(board [][]byte, word string) bool {
   
	res := false
	for i := range board {
		for j := range board[i] {
			visited := make(map[[2]int]bool)
			res = res || dfs(board, word, i, j, visited)
		}
	}

	return res
}

func dfs(board [][]byte, word string, i, j int, visited map[[2]int]bool) bool {
	if len(word) == 0 {
		return true
	}

    if i >= len(board) || i < 0 || j >= len(board[i]) || j < 0 || visited[[2]int{i,j}] {
		return false
	}

	if word[0] != board[i][j] {
		return false
	}

	word = word[1:]
	visited[[2]int{i, j}] = true
    res:= dfs(board, word, i+1, j, visited) || dfs(board, word, i-1, j, visited) || dfs(board, word, i, j+1, visited) || dfs(board, word, i, j-1, visited)
    visited[[2]int{i, j}] = false
    return res
}