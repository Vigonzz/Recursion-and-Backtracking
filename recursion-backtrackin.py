# Violet Gonzalez 

# Assignment 5

def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    
    # Create to record the exact character counts from a matching window
    need = {}
    for character in s1:
        if character not in need:
            need[character] = 1
        else:
            need[character] += 1

    # Building the first window
    window = {}
    for character in s2[:len(s1)]:
        if character not in window:
            window[character] = 1
        else:
            window[character] += 1
    
    # Compare the first window
    if window == need:
        return True
    
    # Slide the window
    for i in range(len(s1), len(s2)):
        entering = s2[i]
        leaving = s2[i - len(s1)]
        if entering not in window:
            window[entering] = 1
        else:
            window[entering] += 1
        window[leaving] -= 1
        # remove empty counts
        if window[leaving] == 0:
            del window[leaving]
            if window == need:
                return True
    return False

# Test our check inclusion function
print("---Test---")

print("\n---Test 1---")
print(check_inclusion("ab", "eidbaooo"))

print("\n---Test 2---")
print(check_inclusion("ab", "eidboaoo"))

print("\n---Test 3---")
print(check_inclusion("abc", "ab"))

print("\n---Test 4---")
print(check_inclusion("abc", "cabxxx"))

print("\n---Test 5---")
print(check_inclusion("abc", "xxxcab"))

print("\n---Test 6---")
print(check_inclusion("aab", "abbab"))

print("\n---Test 7---")
print(check_inclusion("a", "b"))