VBA Challange

    TA's Angel and Megan assisted me:

        Megan: assisted with my initial VBA code when creating a new colum for the ticker names, specifically with deleting duplicates.

        Angel: Assisted when tring to calculate the percentge change, specifically with holding that 'opening price' for a company as the code iterated to find when tickers duplicated. 


    I receive the idea to: 
    
        - 'Call' the Subroutine through out multiple sheets:
  
            https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/call-statement

        - Application.Screen Updating:

            https://learn.microsoft.com/en-us/office/vba/api/excel.application.screenupdating

        - Application.Calculation:

            https://learn.microsoft.com/en-us/office/vba/api/excel.application.calculation

            https://learn.microsoft.com/en-us/office/vba/api/excel.xlcalculation

    The "If Not '____' Is Nothing Then" came from various youtube videos and google searches.




VBA Code:

Sub HW2CALL()

   ' everytime we update via the loops below it "shows on the excel sheet", this will turn off the updates until the calculations are done
   
    Application.ScreenUpdating = False
    
    ' stops excel from automatically re-calculating the formulas after every change is made to a cell, instead in keeps track of the changes and will know which formulas the changes effect, but won't officially calculate until told to
    
    Application.Calculation = xlCalculationManual
    
    Call HW2(ThisWorkbook.Sheets("2018"))
    Call HW2(ThisWorkbook.Sheets("2019"))
    Call HW2(ThisWorkbook.Sheets("2020"))

        Application.ScreenUpdating = True
        
        ' tells Excel to now calculate
        
        Application.Calculation = xlCalculationAutomatic
    
End Sub

Sub HW2(ws As Worksheet)

' (ws As Worksheet) is telling the HW2 subroutine to refer back to HW2 subroutine with the Call functions, so that HW2 can be enacted to all those sheets.

ws.Range("I1").Value = "Ticker"
ws.Range("O1").Value = "Ticker"
ws.Range("P1").Value = "Value"
ws.Range("J1").Value = "Yearly Change"
ws.Range("K1").Value = "Percentage Change"
ws.Range("L1").Value = "Total Stock Volume"
ws.Cells(2, 14).Value = "Greatest % Increase"
ws.Cells(3, 14).Value = "Greatest % Decrease"
ws.Cells(4, 14).Value = "Greatest Volume Total"

Dim Ticker As String

Dim RC As Integer
RC = 2

Dim OpenP As Double

Dim OpenCounter As Double
OpenCounter = 2

Dim CloseP As Double

Dim YC As Double
YC = 0
Dim PC As Double
PC = 0

Dim Vol As Double
Vol = 0

Dim LastRow As Long
LastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

 
For i = 2 To LastRow

    OpenP = ws.Cells(OpenCounter, 3).Value

If ws.Cells(i + 1, 1).Value = ws.Cells(i, 1).Value Or i = LastRow Then

    Vol = Vol + ws.Cells(i, 7).Value

End If

    If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Or i = LastRow Then

        Ticker = ws.Cells(i, 1).Value
        CloseP = ws.Cells(i, 6).Value
        Vol = Vol + ws.Cells(i, 7).Value
       
       PC = ((CloseP - OpenP) / OpenP)
        
        ws.Range("K" & RC).Value = PC
        
        YC = CloseP - OpenP
        
        ws.Range("L" & RC).Value = Vol
        
        ws.Range("J" & RC).Value = YC
        
        If ws.Range("J" & RC).Value > 0 Then
            
                    ws.Range("J" & RC).Interior.ColorIndex = 6
            
                ElseIf ws.Range("J" & RC).Value < 0 Then
                
                      ws.Range("J" & RC).Interior.ColorIndex = 3
                      
                ElseIf ws.Range("J" & RC).Value = 0 Then
                
                      ws.Range("J" & RC).Interior.ColorIndex = 10
                      
            End If
            
        ws.Range("I" & RC).Value = Ticker
        
        RC = RC + 1
        
        OpenCounter = i + 1
        CloseP = 0
        YC = 0
        PC = 0
        Vol = 0
        
    
        
    End If
    
        
Next i

        ' put this outside of the iteration to help code run faster
        Dim rng As Range
        Set rng = ws.Range("K:K")
        rng.NumberFormat = "0%"

Dim rng2 As Range
Set rng2 = ws.Range("P2:P3")


Dim MaxVal As Double
Dim MinVal As Double
Dim MaxValV As Double

Dim TickerMax As String
Dim TickerMin As String
Dim TickerMaxValV As String

Dim LastRow2 As Long
LastRow2 = ws.Cells(ws.Rows.Count, 11).End(xlUp).Row
Dim LastRow3 As Long
LastRow3 = ws.Cells(ws.Rows.Count, 12).End(xlUp).Row

Dim rng3 As Range
Set rng3 = ws.Range("K2:K" & LastRow2)

Dim rng4 As Range
Set rng4 = ws.Range("L2:L" & LastRow3)

Dim Maxcell As Range

' this goes through the K column (starting at K2 and ending at the LastRow2) and finds the max value within this column and assings to MaxVal
MaxVal = Application.WorksheetFunction.Max(ws.Range("K2:K" & LastRow2))

' for each loop goes through each cell in rng3(column K), if the cell within this range is equal to the MaxVal previously found, it assings it to variable MaxCell
For Each Cell In rng3

        If Cell.Value = MaxVal Then
            Set Maxcell = Cell
            Exit For

        End If
        
Next Cell

' if there is no cell in rng3 whose value equals the MaxVal, MaxCell would not get assigned and remain "Nothing"
' if I tried to access the value porperty for Maxcell then I would get an error bc the value for the range-variable MaxCell would be "nothing"
' this "if not" function checks if Maxcell is nothing, if it is something (not nothing) which the pervious statement would make something equal to the MaxVal, i can use the MaxCell properties like value
' if mutiple MaxVal cells found, it will set MaxCell to the first cell value found and row found in the 'For Each' loop
' if I wanted to capture all the cells with the max value, i could set up a 'collection' (too advance for me now)

        If Not Maxcell Is Nothing Then

        ws.Cells(2, 16).Value = Maxcell.Value
        TickerMax = ws.Cells(Maxcell.Row, 9).Value
        ws.Cells(2, 15).Value = TickerMax
        End If

Dim Mincell As Range

MinVal = Application.WorksheetFunction.Min(ws.Range("K2:K" & LastRow2))

For Each Cell2 In rng3

        If Cell2.Value = MinVal Then
            Set Mincell = Cell2
            Exit For

        End If
        
Next Cell2

        If Not Mincell Is Nothing Then

        ws.Cells(3, 16).Value = Mincell.Value
        TickerMin = ws.Cells(Mincell.Row, 9).Value
        ws.Cells(3, 15).Value = TickerMin
        End If

rng2.NumberFormat = "0%"


Dim MaxValVCell As Range

MaxValV = Application.WorksheetFunction.Max(ws.Range("L1:L" & LastRow3))

For Each Cell3 In rng4

        If Cell3.Value = MaxValV Then
            Set MaxValVCell = Cell3
            Exit For

        End If
        
Next Cell3

        If Not MaxValVCell Is Nothing Then
        
        ws.Cells(4, 16).Value = MaxValVCell.Value
        TickerMaxValV = ws.Cells(MaxValVCell.Row, 9).Value
        ws.Cells(4, 15).Value = TickerMaxValV
        
        End If
 

End Sub
