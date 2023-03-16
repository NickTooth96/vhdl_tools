-------------------------------------------------------------------------
-- CREATOR
-- Department of Electrical and Computer Engineering
-- Iowa State University
-------------------------------------------------------------------------
-- tb_NAME.vhd
-------------------------------------------------------------------------
-- DESCRIPTION
-- NOTES:
-- DATE by CREATOR::Design created.
-------------------------------------------------------------------------

LIBRARIES

entity tb_NAME  is

  GENERICS

end tb_NAME ;

architecture behavior of tb_NAME  is  
-- Calculate the clock period as twice the half-period
constant cCLK_PER  : time := gCLK_HPER * 2;


  component NAME is

    PORTS

  end component;

-- Temporary signals to connect to the NAME component.
	
SIGNALS

begin

PORTMAP

  -- This process sets the clock value (low for gCLK_HPER, then high
  -- for gCLK_HPER). Absent a "wait" command, processes restart 
  -- at the beginning once they have reached the final statement.
  P_CLK: process
  begin
    s_CLK <= '0';
    wait for gCLK_HPER;
    s_CLK <= '1';
    wait for gCLK_HPER;
  end process;
  
  -- Testbench process  
  P_TB: process

    begin
TESTCASES
    wait;

  end process;
  
end behavior;