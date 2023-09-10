def get_input(filename):
   rows = []
   try:

        with open(filename, 'r') as f:

            for line in f.readlines():

                rows.append(line)
                
   except OSError as e:

        print(f"Unable to open {filename}: {e}")

        raise 
    

    
   return rows

        