from enum import Enum


class ServiceType(Enum):
    Regular_Parcel = "DOM.RP"
    Expedited_Parcel = "DOM.EP"
    Xpresspost = "DOM.XP"
    Priority = "DOM.PC"
    Library_Books = "DOM.LIB"
    Expedited_Parcel_USA = "USA.EP"
    Priority_Worldwide_Envelope_USA = "USA.PW.ENV"
    Priority_Worldwide_pak_USA = "USA.PW.PAK"
    Priority_Worldwide_Parcel_USA = "USA.PW.PARCEL"
    Small_Packet_USA_Air = "USA.SP.AIR"
    Tracked_Packet_USA = "USA.TP"
    Tracked_Packet_USA_LVM = "USA.TP.LVM"
    Xpresspost_USA = "USA.XP"
    Xpresspost_International = "INT.XP"
    International_Parcel_Air = "INT.IP.AIR"
    International_Parcel_Surface = "INT.IP.SURF"
    Priority_Worldwide_Envelope_Intl = "INT.PW.ENV"
    Priority_Worldwide_pak_Intl = "INT.PW.PAK"
    Priority_Worldwide_parcel_Intl = "INT.PW.PARCEL"
    Small_Packet_International_Air = "INT.SP.AIR"
    Small_Packet_International_Surface = "INT.SP.SURF"
    Tracked_Packet_International = "INT.TP"


class OptionCode(Enum):
    Signature = "SO"
    Coverage = "COV"
    Collect_on_delivery = "COD"
    Proof_of_Age_Required_18 = "PA18"
    Proof_of_Age_Required_19 = "PA19"
    Card_for_pickup = "HFP"
    Do_not_safe_drop = "DNS"
    Leave_at_door = "LAD"
    Deliver_to_Post_Office = "D2PO"
    Return_at_Senders_Expense = "RASE"
    Return_to_Sender = "RTS"
    Abandon = "ABAN"