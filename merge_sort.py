def merge_sort(contact_list):
    """Sort a list of contacts alphabetically by name."""
    if len(contact_list) <= 1:
        return contact_list

    mid = len(contact_list) // 2
    left_half = merge_sort(contact_list[:mid])
    right_half = merge_sort(contact_list[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].name.lower() <= right[j].name.lower():
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining items
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list
