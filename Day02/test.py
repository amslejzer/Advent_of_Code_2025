text = "111112"
for i in range(1,len(text)//2+1):
    pattern = text[:i]
    pat_count = text.count(pattern)
    print(f"Pattern: {pattern} | Count: {pat_count}")
    if(pat_count == len(text)/len(pattern)):
        print("Hits")