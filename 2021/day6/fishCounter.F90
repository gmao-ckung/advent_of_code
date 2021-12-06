recursive function fishLifeCounter(fishTimer, days) result(numFish)
   integer, intent(in):: fishTimer, days
   integer :: newFishTimer, newDays
   integer*8 :: numFish

   newFishTimer = fishTimer - 1
   newDays = days - 1

   if (newFishTimer > newDays) then
       numFish = 1
       return
   else if (newDays == 0) then
        if (newFishTimer >= 0) then
            numFish = 1
            return
        else
            numFish = 2
            return
        endif
   else
        if (newFishTimer >= 0) then
            numFish = fishLifeCounter(newFishTimer, newDays)
            return
        else
            numFish = fishLifeCounter(6, newDays) + fishLifeCounter(8, newDays)
            return
        endif
    endif
end function fishLifeCounter

program fishCounter
   implicit none

   integer :: fishID = 0
   integer :: numDays

   integer :: numFish, fishLifeCounter
   real :: t1, t2

   numDays = 256

   call cpu_time(t1)
   numFish = fishLifeCounter(0, numDays)
   write(*,*) "Number of fish = ", numFish
   numFish = fishLifeCounter(1, numDays)
   write(*,*) "Number of fish = ", numFish
   numFish = fishLifeCounter(2, numDays)
   write(*,*) "Number of fish = ", numFish
   numFish = fishLifeCounter(3, numDays)
   write(*,*) "Number of fish = ", numFish
   numFish = fishLifeCounter(4, numDays)
   write(*,*) "Number of fish = ", numFish
   numFish = fishLifeCounter(5, numDays)
   write(*,*) "Number of fish = ", numFish
   call cpu_time(t2)

   write(*,*) "Execution time = ", t2-t1

end program
