unsorted = [1,5,7,4,10,8,3,2,0,6];

function selection(array)  {
  for (i = 0; i < array.length; i++)  {
      selected = 0;
    for (j = 0; j < array.length-1; j++)  {
      if (array[selected] > array[i+1]) {
        temp = array[selected];
        array[selected] = array[i+1];
        array[i+1] = temp;
      }
      selected++;
    } 
  }
  return array;
}


console.log("Unsorted array: " + unsorted);
sorted = selection(unsorted);
console.log("Sorted array: " + sorted);