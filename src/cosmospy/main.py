import cosmospy

if __name__ == '__main__':
    #pip uninstall cosmospy
    # pip install git+https://www.github.com/timetrp/cosmospy
    print("reload")
    # imp.reload(cosmospy)
    
    query = cosmospy.Query()
    resp = query.get_pools()
