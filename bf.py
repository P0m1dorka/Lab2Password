
import stubs

def read_file(file_name: str):
   with open(file=file_name, mode='r') as file:
      while content := file.readline():
         yield content
      
          
          
def brute(file_read:str):
      reader_generator= read_file(file_read)
      a1=next(reader_generator)
      try_pass=a1.strip('\n')
      return try_pass
      