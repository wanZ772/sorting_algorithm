raw_data = [7,4,2,5,0];

for (i = 0; i < raw_data.length; i++) {
  j = i;
  while (j > 0) {
    console.log("point: "+ j + " --> " + raw_data);
    if (raw_data[j] < raw_data[j-1])  {
      temp = raw_data[j];
      raw_data[j] = raw_data[j-1];
      raw_data[j-1] = temp;
    }
    j--;
  }
}
console.log("Sorted: " + raw_data);