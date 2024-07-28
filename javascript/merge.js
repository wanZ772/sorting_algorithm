unsorted = [1,5,7,4,10,8,3,2,0,6];


function divide(array)  {
  n = array.length;
  
  if (n == 1) {
    return array;
  } else  {
    let mid = parseInt(n / 2);
    let left = array.slice(0, mid);
    let right = array.slice(mid);
    
    return merge(divide(left), divide(right));
    
  }
}

function merge(left, right) {
  left_point = 0; right_point = 0;
  left_length = left.length; right_length = right.length;
  
  sorted_ = [];
  
  while ((left_point < left_length) && (right_point < right_length))  {
    if (left[left_point] < right[right_point])  {
      sorted_.push(left[left_point]);
      left_point++;
    } else  {
      sorted_.push(right[right_point]);
      right_point++;
    }
  }
  
  while (left_point < left_length)  {
    sorted_.push(left[left_point]);
      left_point++;
  }
  
  while (right_point < right_length)  {
    sorted_.push(right[right_point]);
      right_point++;
  }
  
  return sorted_;
  
}

console.log("Unsorted array: " + unsorted)
sorted = divide(unsorted)
console.log("Sorted array: " + sorted)