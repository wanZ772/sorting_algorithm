raw_data = [7,4,2,5,0];

for (i = 0; i < raw_data.length; i++) {
  for (j = 0; j < raw_data.length -1; j++)  {
    if (raw_data[j] > raw_data[j+1])  {
      temp = raw_data[j+1];
      raw_data[j+1] = raw_data[j];
      raw_data[j] = temp;
    }
  }
}
console.log("Sorted: " + raw_data);