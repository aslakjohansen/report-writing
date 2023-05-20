defmodule Fibonacci do
  def fib(0) do
    0
  end
  
  def fib(1) do
    1
  end
  
  def fib(n) when n>0 do
    fib(n-1) + fib(n-2)
  end
end
