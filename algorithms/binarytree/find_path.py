#coding=utf-8
#=========================================================
#     Copyright (C) 2019 Shanghaitech SVIP Lab. All rights reserved.
#     
#     ScriptName: find_path.py
#     Author: Lina Hu
#     CreatedDate: Thu 30 May 2019 08:08:36 AM CST
#     
#=========================================================
def FindPath(self, root, expectNumber):
        # write code here
        
        paths_l = []
        path = []
        len_l = []
        if root is None: return None
        
        def findloc(len_l, path_len):
            l = 0
            r = max(len_l) 
            while(l<=r):
                mid = (l+r)/2
                if len_l[mid] < path_len:
                    l = mid + 1
                elif len_l[mid] > path_len:
                    r = mid - 1                    
                else:
                    r = mid
                    break
            if len_l[r] < path_len:
                r += 1
            
            return r 
        
        def get_path(root, numb, paths_l, len_l, path):
            if root is None or root.val < numb: return 
            n_path = path.copy()
            n_path.append(root.val)
            res_v = numb-root.val
            if res_v == 0:
                if not len_l:
                    paths_l.append(n_path)
                    len_l.append(len(n_path))
                else:
                    path_len = len(n_path)
                    idx = findloc(len_l, path_len)
                    paths_l.insert(idx, n_path)
                    len_l.insert(idx, path_len)
                return 
            get_path(root.left, res_v, paths_l, len_l, n_path)
            get_path(root.right, res_v, paths_l, len_l, n_path)
            
            return
        
        get_path(root, expectNumber, paths_l, len_l, path)
        
        return paths_l
