raw_data = [7,4,2,5,0];


function merge(data)  {
  n = data.length;
  
  if (n == 1) {
    return data;
    
  } else  {
    mid = parseInt(n / 2);
    left = [];
    right = [];
    for (i = 0; i < n; i++) {
      if (i < mid)  {
        left.push(data[i]);
      } else  {
        right.push(data[i]);
      }
    }
    
    
    merge(right);
    merge(left);
    
    left_point = 0; right_point = 0;
    
    left_length = left.length;
    right_length = right.length;
    
    sorted_data = [];
    
    while ((left_point < left_length) && (right_point < right_length))  {
      if (left[left_point] < right[right_point])  {
        sorted_data.push(left[left_point]);
        left_point++;
      } else  {
        sorted_data.push(right[right_point]);
        right_point++;
      }
    }
    
    while (left_point < left_length)  {
        sorted_data.push(left[left_point]);
        left_point++;
    }
    
    while (right_point < right_length)  {
        sorted_data.push(right[right_point]);
        right_point++;
    }
    
    return sorted_data;
  }
}

sorted_ = merge(raw_data);

console.log("Sorted: " + sorted_);