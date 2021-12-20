from carefood.carefood_parser.carefood_producer import main
from time import time


if __name__ == "__main__":
    print("Start producer...")
    start_time = time()
    main()
    print("END")
    print(f"Spend time : {time() - start_time}")
