-------------------------------------------------------------------------
-- {creator}
-- Department of Electrical and Computer Engineering
-- Iowa State University
-------------------------------------------------------------------------


-- tb_{name}.vhd
-------------------------------------------------------------------------
-- DESCRIPTION: {description}
-- NOTES:
-- {date} by {creator}::Design created.
-------------------------------------------------------------------------

library IEEE;
use IEEE.std_logic_1164.all;

entity tb_{name} is

  generic(	gCLK_HPER   	: time := 50 ns);

end tb_{name};

architecture behavior of tb_{name} is
  
  -- Calculate the clock period as twice the half-period
  constant cCLK_PER  : time := gCLK_HPER * 2;


  component {name}

    	{port}

  end component;

  -- Temporary signals to connect to the dff component.
	
	{signals}

begin

  test_{name} : {name}
  {port_map}

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

		{test_cases}

    	wait;

  end process;
  
end behavior;