C = [   [15, -2, -3, -1, 0, -6],
        [-2,-15, 0,  1, 3,   8],
        [ 3, -9, 0,  2, 0, -15],
        [ 1,  1, 2, -6, 2,   0],
        [ 0,  3, 0,  2, -9, 16]
       ]; % Form the augmented matrix [A|b]

[rows, cols] = size(C); % Get the number of rows and columns in the augmented matrix

for j = 1:cols - 1 % Loop through each column except the last one (the augmented part)
    i = j;
    [max_val, pivotIdx] = max(abs(C(i:end, j))); % Max returns max value, but if used with 2 args, also returns idx
    idx = pivotIdx + i - 1; % Adjust the index to account for the starting point of the search, -1 because MATLAB does not 0-index matrices

    if idx ~= i % Row swapping
        temp = C(j, 1:end);
        C(j, 1:end) = C(idx, 1:end);
        C(idx, 1:end) = temp;
    end
    %display("Matrix after swapping")
    %C
 

    C(j, 1:end) = C(j, 1:end) / C(j,j);
    %display("Matrix after dividing 1")
    %C
    for p = 1:rows
      if p == j
        continue
      end
      C(p, 1:end) = C(p, 1:end) - (C(p, j) * C(j, 1:end));
    end
    %display("Matrix after dividing 2")
    %C
    %display('----------------------------------------------')
end

C