import math

def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

branches = {'Uttara Branch': (23.8728568, 90.3984184),
 'City Bank Airport': (23.8513998, 90.3944536),
 'City Bank Nikunja': (23.8330429, 90.4092871),
 'City Bank Beside Uttara Diagnostic': (23.8679743, 90.3840879),
 'City Bank Mirpur 12': (23.8248293, 90.3551134),
 'City Bank Le Meridien': (23.827149, 90.4106238),
 'City Bank Shaheed Sarani': (23.8629078, 90.3816318),
 'City Bank Narayanganj': (23.8673789, 90.429412),
 'City Bank Pallabi': (23.8248938, 90.3549467),
 'City Bank JFP': (23.813316, 90.4147498)}

branch_names = list(branches.keys())
visited_branches = [branch_names[0]]
total_distance = 0
branch_distances = {key: {} for key in branch_names}

for i, current_branch in enumerate(branch_names):
    for next_branch in branch_names[i + 1:]:
        dist = euclidean_distance(branches[current_branch], branches[next_branch])
        branch_distances[current_branch][next_branch] = dist
        branch_distances[next_branch][current_branch] = dist

for current_branch in branch_names[1:]:
    sorted_distances = sorted(branch_distances[current_branch].items(), key=lambda x: x[1])
    for next_branch, distance in sorted_distances:
        if next_branch not in visited_branches:
            visited_branches.append(next_branch)
            total_distance += distance
            break

print(total_distance, visited_branches)

# 0.1668846023243121 ['Uttara Branch', 'City Bank Shaheed Sarani', 'City Bank Le Meridien', 'City Bank Airport', 'City Bank Pallabi', 'City Bank Nikunja', 'City Bank Beside Uttara Diagnostic', 'City Bank JFP', 'City Bank Mirpur 12', 'City Bank Narayanganj']