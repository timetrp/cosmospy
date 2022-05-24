import cosmospy

if __name__ == '__main__':
    
    print("reload")
    # imp.reload(cosmospy)
    
    query = cosmospy.Query()
    resp = query.get_pools()
