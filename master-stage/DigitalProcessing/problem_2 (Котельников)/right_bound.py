function y = FindRightBound(X,W)
  A = 0.05*max(X);
  for i=1:length(X)
    if X(i)<=A
        y = W(i);
        return;
    end
  end
end