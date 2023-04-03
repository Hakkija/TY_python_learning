def get_dance_pairs(boys_heights, girls_heights):
    boys_heights.sort(reverse=True)
    girls_heights.sort(reverse=True)
    pairs = list(zip(boys_heights[:len(girls_heights)], girls_heights))
    remaining_boys = boys_heights[len(girls_heights):]
    return pairs, remaining_boys

def main():
    # Get heights from the user
    boys_heights = list(map(int, input("Enter the boys' heights: ").split()))
    girls_heights = list(map(int, input("Enter the girls' heights: ").split()))

    # Get dance pairs and remaining boys (if any)
    dance_pairs, remaining_boys = get_dance_pairs(boys_heights, girls_heights)

    # Output the dance pairs
    print("Dance pairs are:", " ".join(str(pair) for pair in dance_pairs))

    # Output the remaining boys (if any)
    if remaining_boys:
        print("Boys with heights of", ", ".join(map(str, remaining_boys)), "were left without a partner.")

main()
