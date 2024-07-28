unsorted = [1,5,7,4,10,8,3,2,0,6];

function quick(array)  {
   n = array.length;
  if (n < 2) {
    return array;
  } else  {
    let left = [];
    let right = [];
    let pivot = array[n - 1];
    for (let i = 0; i < n - 1; i++) {
      if (array[i] < pivot) {
        left.push(array[i]);
      } else  {
        right.push(array[i]);
      }
    }
    
    return [...quick(left), pivot, quick(right)];
    
  }
}


console.log("Unsorted array: " + unsorted);
sorted = quick(unsorted);
console.log("Sorted array: " + sorted);