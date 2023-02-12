// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.11;

// Import thirdweb contracts
import "@thirdweb-dev/contracts/drop/DropERC1155.sol";
import "@thirdweb-dev/contracts/token/TokenERC20.sol";
import "@thirdweb-dev/contracts/openzeppelin-presets/utils/ERC1155/ERC1155Holder.sol";

// Import OpenZeppelin
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract thirdwebGame is ReentrancyGuard, ERC1155Holder {

    TokenERC20 public immutable ethy; 
    address owner; 

    uint256 industryType; 
    struct cap{
        uint256 slab1; 
        uint256 slab2; 
        uint256 slab3; 
        uint256 slab4; 
    }
    mapping(industryType=>cap) public industryCap;

    constructor (TokenERC20 _tokenAddress){
        owner = msg.sender; 
        ethy = _tokenAddress; 
    }

    // mapping (address => mapValue) public playerTool;
    // mapping (address => mapValue) public playerLastUpdate; 

    function stake(uint256 _tokenId) external nonReentrant {
        
        require(toolsCollection.balanceOf(msg.sender, _tokenId)>=1, "You must have atleast 1 of the tools you are trying to stake"); 

        if(playerTool[msg.sender].isData){
            toolsCollection.safeTransferFrom(address(this), msg.sender, playerTool[msg.sender].value, 1, "Returning your old tool"); 
        }

        uint256 reward = calculateRewards(msg.sender); 
        mustuCoins.transfer(msg.sender, reward); 
        
        toolsCollection.safeTransferFrom(msg.sender, address(this), _tokenId, 1, "Staking your tool"); 

        playerTool[msg.sender].value = _tokenId; 
        playerTool[msg.sender].isData = true; 

        playerLastUpdate[msg.sender].value = block.timestamp; 
        playerLastUpdate[msg.sender].isData = true;

    }

    function calculateRewards(address _player) public view returns (uint256 _rewards) {
        
        if(!playerLastUpdate[_player].isData || !playerTool[_player].isData){
            return 0; 
        }

        uint256 timeDifference = block.timestamp - playerLastUpdate[_player].value; 

        uint256 rewards = timeDifference * 10_000_000_000_000 * (playerTool[_player].value+1);

        return rewards; 
    }

    function setCap(uint256 _industryType, uint256 _s1, uint256 _s2, uint256 _s3, uint _s4) public {
        cap storage newCap = industryCap[_industryType];
        newCap.slab1 = _s1; 
        newCap.slab1 = _s1; 
        newCap.slab1 = _s1; 
        newCap.slab1 = _s1; 
    }

    function getEty(uint256 emission) external nonReentrant{
        uint256 reward = calculateRewards(emission);
        ethy.transfer(msg.sender, reward);  
    }

    function calculateRewards(uint256 emission) public pure returns(uint256 _rewards){
       
        cap storage thisCap = industryCap[_industryType];
        uint256 reward = 0; 

        if(emission < 10){
            reward = (25-emission)*10; 
        }
        else if(emission >=10 && emission<15){
            reward = (25-emission)*5; 
        }
        else if(emission >=15 && emission<25){
            reward = (25-emission); 
        }
        else{
            reward = 0; 
        }
    }

    //     if(emission<25){
    //         if(emission>0 && emission<10){

    //             reward = (10-n)*100; 

    //             //erc token logic
    //             // forward tokens= (10-n)*100 tokens
    //             // for every token company will get tax exempt of 0.1%
    //             // totaltax -= (0.1*token)*totaltax/100;
    //             // or transfer

    //             return 0;
    //         }
    //         else if(n>=10 && n<15){
    //             taxes+=15;
    //             return taxes;
    //         }
    //         else if(n>=15){
    //             taxes+=30;
    //             return taxes;
    //         }
    //     }
    //     else{
    //         taxes= (30+ ((n-25)*20));
    //         return taxes;
    //     }     
    // }

}