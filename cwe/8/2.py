with open('data.txt') as f:
    forest = f.read().splitlines()

dim_forest = len(forest)
visible_trees = 0
max_vis_score = 1
for row in range(dim_forest):
    for col in range(dim_forest):
        visible_l = 0
        l_col = col - 1
        while l_col >= 0:
            visible_l += 1
            if forest[row][l_col] >= forest[row][col]:
                break
            l_col -= 1

        visible_r = 0
        r_col = col + 1
        while r_col < dim_forest:
            visible_r += 1
            if forest[row][r_col] >= forest[row][col]:
                break
            r_col += 1

        visible_u = 0
        u_row = row - 1
        while u_row >= 0:
            visible_u += 1
            if forest[u_row][col] >= forest[row][col]:
                break
            u_row -= 1

        visible_d = 0
        d_row = row + 1
        while d_row < dim_forest:
            visible_d += 1
            if forest[d_row][col] >= forest[row][col]:
                break
            d_row += 1

        if row == 0 or row == dim_forest or col == 0 or col == dim_forest:
            vis_score = 0
        else:
            vis_score = visible_l * visible_r * visible_u * visible_d
        if vis_score > max_vis_score:
            max_vis_score = vis_score
print(f'Max Vis Score: {max_vis_score}')
