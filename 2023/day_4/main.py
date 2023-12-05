test_data="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def read_input(file="input.txt"):
    with open(file) as f:
        lines = f.readlines()
        content = []
    for line in lines:
        content.append(line.strip())
    
    return(content)

def part_1():
    # data = test_data.splitlines()
    data = read_input()
    total = []
    for line in data:
        points = 0
        card, numbers = line.split(":") 
        wining, yours = numbers.split("|")
        wining= wining.split()
        yours = yours.split()
        for number in wining:
            if number in yours:
                if points > 0: 
                    points = points*2
                else: 
                    points = 1
        print(f"{card}: {points}")
        total.append(int(points))
    print(f"Total: {sum(total)}")
    
# end def

def part_2():
    data = test_data.splitlines()
    data = read_input()
    total = []
    scratch_pad = {}
    total_cards = {}
    for line in data:
        won_cards = 0
        card, numbers = line.split(":") 
        wining, yours = numbers.split("|")
        wining= wining.split()
        yours = yours.split()
        card_id = int(card.split()[1])
        total_cards.update({
            card_id:{"total":1}
        })
        for number in wining:
            if number in yours:
                won_cards = won_cards + 1
                total_cards[card_id]["total"]+=1
        
        # print(won_cards)
        ids=[]
        for i in range(won_cards):
            ids.append(card_id + i + 1)
        
        scratch_pad.update({
            int(card_id):{
                "cards": ids,
                "won_cards": len(ids)
            }
        })
    
    print(scratch_pad)
    print("--------------------------")
    
    for detail in scratch_pad:
        print(f"Processing: {detail}")


    for detail in scratch_pad: 
        print(f"Processing card: {detail}")
        for card in scratch_pad[detail]["cards"]:
            # print(f'Won cards: {scratch_pad[card]["cards"]}')
            
            while len(scratch_pad[card]["cards"] ) > 0:
                won_card = scratch_pad[card]["cards"].pop(0)
                # print(f'Processing {won_card}, last_sum: {total_cards}')
                
                total_cards[won_card]["total"]+=1
                # print(f'Won cards: {scratch_pad[won_card]["cards"]}')
                
                for ele in scratch_pad[won_card]["cards"]: 
                    # print("processing")
                    scratch_pad[card]["cards"].append(ele)
                    total_cards[won_card]["total"]+=1
            
            print(f'Processed: {scratch_pad[card]["cards"]}')
    
    print(total_cards)
    print(sum([ x['total'] for x in total_cards.values()]))
        
    
    

def main():
    part_1()
    part_2()

# end def


if __name__ == "__main__":
    main()
# end main