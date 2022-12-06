"use strict";
exports.__esModule = true;
var fs = require("fs");
var test_data = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"];
var input_data = fs.readFileSync('./day_6/input.txt', 'utf8');
function decoder(signal, size) {
    var found = false;
    for (var _i = 0; _i < signal.length; _i++) {
        var buffer = [];
        for (var _j = _i; _j < _i + size; _j++) {
            if (buffer.length < size && !found) {
                if (!buffer.includes(signal[_j])) {
                    buffer.push(signal[_j]);
                    if (buffer.length == size) {
                        console.log('Handshake till ', _j, ' message start at: ', _j + 1);
                        found = true;
                        break;
                    }
                }
            }
            else {
                break;
            }
        }
    }
}
// console.log(input_data)
decoder(input_data, 4);
decoder(input_data, 14);
