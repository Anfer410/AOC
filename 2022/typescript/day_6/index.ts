import * as fs from 'fs';


const test_data: Array<string> = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
"bvwbjplbgvbhsrlpgdmjqwftvncz",
"nppdvjthqldpwncqszvftbrmjlhg",
"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]



let input_data = fs.readFileSync('./day_6/input.txt', 'utf8');


function decoder(signal, size){
    let found = false
    

    for(var _i=0; _i < signal.length; _i++){
        let buffer: Array<string> = []
        
        for(var _j=_i;_j < _i + size; _j++ ){
            if(buffer.length < size && !found ){
                if(!buffer.includes(signal[_j])){
                    buffer.push(signal[_j])
                    
                    if(buffer.length == size){
                        console.log('Handshake till ', _j, ' message start at: ',_j + 1)
                        found = true
                        break
                    }
                }
            } else {
                break
            }

        }
    }
}


decoder(input_data,4)  // Part 1
decoder(input_data,14) // Part 2







