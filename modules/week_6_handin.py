import urllib.request
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

class NotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)

class Week6():
    def __init__(self, url_list=[]):
        self.url_list= url_list
        self.filenames = Week6.multi_download(Week6.download, url_list)

    def download(url):
       
        filename = url.rsplit('/', 1)[1]
        try:
            print("downloading...")
            downloaded_file = urllib.request.urlretrieve(url,'./output_data/'+filename)
            print("download done")
            print('filepath: ',downloaded_file)
            return filename
        except NotFoundException as nfe:
            print(nfe)

    def multi_download(func, urls, workers=5):
        with ThreadPoolExecutor(workers) as ex:
            res = ex.map(func, urls)
        return list(res)

    def __iter__(self):
        return self
    
    def __next__(self):
        i = 0
        if i <= len(self.url_list):
            result = self.url_list[i]
            i = i + 1
            return result
        else:
            raise StopIteration
            
    def urllist_generator(self):
        for url in url_list:
            yield url

    def avg_vowels(filename):
        vovels = ('aeiouyAEIOUY')
        word_count = 0
        vovel_count = 0
        with open (filename,'r') as text:
            for line in text.readlines():
                for word in line:
                    word_count +=1
                    for character in word:
                        if character in vovels:
                            vovel_count += 1
        return word_count/vovel_count
        
    def multiprocess(self,func, args, workers=3):
        new_args = []
        for arg in args:
            arg = './output_data/' + arg
            new_args.append(arg)
        with ProcessPoolExecutor(workers) as ex:
            res = ex.map(func, new_args)
        return list(res)
    
    def hardest_read(self):
        res = self.multiprocess(Week6.avg_vowels, self.filenames)
        dicto={res[i]: './output_data/'+self.filenames[i] for i in range(len(res))}
        sorted_dicto = sorted(dicto.items(), key=lambda item: item[0])
        return sorted_dicto[-1]